import pytest

from utils.precios import GestorPrecios, obtener_precios_respaldo
from utils.scraper import SupermarketScraper


class TestCalcularCostoLista:
    def setup_method(self):
        self.gestor = GestorPrecios()
        self.gestor.ciudad = "Bogota"
        self.gestor.precios = {
            "tomate": {
                "precio_base": 3500,
                "fuente": "respaldo",
                "supermercado": None,
                "confianza": "media",
            },
            "huevo": {
                "precio_base": 550,
                "fuente": "respaldo",
                "supermercado": None,
                "confianza": "media",
            },
            "leche": {
                "precio_base": 3200,
                "fuente": "respaldo",
                "supermercado": None,
                "confianza": "media",
            },
        }

    def test_costo_peso_divide_por_1000(self):
        lista = {"tomate": {"cantidad": 1000, "unidad": "gr", "tipo": "peso"}}
        resultado = self.gestor.calcular_costo_lista(lista)
        assert resultado["total"] == 3500
        assert resultado["desglose"]["tomate"]["costo"] == 3500

    def test_costo_unidad_multiplica_directo(self):
        lista = {"huevo": {"cantidad": 10, "unidad": "unidades", "tipo": "unidad"}}
        resultado = self.gestor.calcular_costo_lista(lista)
        assert resultado["total"] == 5500

    def test_costo_volumen_divide_por_1000(self):
        lista = {"leche": {"cantidad": 2000, "unidad": "ml", "tipo": "volumen"}}
        resultado = self.gestor.calcular_costo_lista(lista)
        assert resultado["total"] == 6400

    def test_factor_ciudad(self):
        self.gestor.ciudad = "Medellin"
        lista = {"tomate": {"cantidad": 1000, "unidad": "gr", "tipo": "peso"}}
        resultado = self.gestor.calcular_costo_lista(lista)
        assert resultado["total"] == round(3500 * 0.95)

    def test_producto_sin_precio_usa_respaldo_o_default(self):
        lista = {"producto_inexistente": {"cantidad": 1, "unidad": "unidad", "tipo": "unidad"}}
        resultado = self.gestor.calcular_costo_lista(lista)
        assert resultado["desglose"]["producto_inexistente"]["fuente"] == "respaldo"
        assert resultado["total"] == 5000


class TestScraperUnidades:
    def setup_method(self):
        self.scraper = SupermarketScraper()

    def test_normalizar_peso_paquete_a_kg(self):
        precio = self.scraper.normalizar_precio_paquete("pan_integral", 3600)
        assert precio == pytest.approx((3600 / 450) * 1000, rel=0.01)

    def test_normalizar_unidad_huevo(self):
        precio = self.scraper.normalizar_precio_paquete("huevo", 16500)
        assert precio == pytest.approx(550, rel=0.01)

    def test_calcular_costo_item_peso(self):
        costo = self.scraper._calcular_costo_item(3500, {"cantidad": 500, "tipo": "peso"})
        assert costo == 1750

    def test_calcular_costo_item_unidad(self):
        costo = self.scraper._calcular_costo_item(550, {"cantidad": 4, "tipo": "unidad"})
        assert costo == 2200


class TestRespaldo:
    def test_todos_los_productos_inventario_tienen_respaldo_o_catalogo(self):
        from data.inventory import InventoryManager
        from data.menu_generator import MenuGenerator
        from data.menu_fijo import DIAS_PLAN
        from utils.producto_catalogo import PRODUCTOS_BUSQUEDA

        mg = MenuGenerator(dias=DIAS_PLAN, personas=2)
        inv = InventoryManager(mg.cargar_menu_fijo())
        respaldo = obtener_precios_respaldo()
        for producto in inv.inventario_necesario:
            assert producto in respaldo or producto in PRODUCTOS_BUSQUEDA
