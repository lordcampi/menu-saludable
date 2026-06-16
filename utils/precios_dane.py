"""Compatibilidad con código que importaba PreciosActualizados."""

from utils.precios import GestorPrecios, obtener_precios_respaldo


class PreciosActualizados(GestorPrecios):
    """Alias retrocompatible. Usar GestorPrecios en código nuevo."""

    def __init__(self):
        super().__init__()
        self.precios_legacy = obtener_precios_respaldo()

    def _obtener_precios_semanales(self):
        return self.precios_legacy

    def ajustar_precios_por_ciudad(self, ciudad):
        factor = super().ajustar_precios_por_ciudad(ciudad)
        for producto in self.precios_legacy:
            self.precios_legacy[producto] = round(self.precios_legacy[producto] * factor)
        return factor
