"""
Módulo de miembros del hogar.

Gestiona los integrantes del hogar con sus factores de consumo.
Soporta activación/desactivación dinámica de miembros sin afectar
la lógica de recetas, inventario o lista de mercado.

FACTOR_BASE_REFERENCIA = 2.0
Corresponde a Julián (1.0) + Annmar (1.0), el escenario original.
Todas las recetas están escritas para este factor base.
El escalado se calcula como: factor_actual / FACTOR_BASE_REFERENCIA.
"""

import json
import os
from typing import Any, Dict, List, Optional

PERSISTENCIA_FILE = "data/hogar_persistencia.json"

FACTOR_BASE_REFERENCIA = 2.0

MIEMBROS_DEFAULT: List[Dict[str, Any]] = [
    {
        "id": "julian",
        "nombre": "Julián",
        "edad": 35,
        "peso": 80,
        "sexo": "hombre",
        "altura": 1.80,
        "objetivo": "mantener",
        "factor_consumo": 1.0,
        "activo": True,
    },
    {
        "id": "annmar",
        "nombre": "Annmar",
        "edad": 30,
        "peso": 58,
        "sexo": "mujer",
        "altura": 1.60,
        "objetivo": "bajar_peso",
        "peso_objetivo": 50,
        "factor_consumo": 1.0,
        "activo": True,
    },
    {
        "id": "nilsa",
        "nombre": "Nilsa",
        "edad": 65,
        "peso": 45,
        "sexo": "mujer",
        "altura": 1.55,
        "objetivo": "mantener",
        "factor_consumo": 0.50,
        "activo": False,
    },
]


def _cargar_persistencia() -> Optional[Dict[str, Any]]:
    """Carga la persistencia de activación de miembros."""
    if not os.path.exists(PERSISTENCIA_FILE):
        return None
    try:
        with open(PERSISTENCIA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _guardar_persistencia(data: Dict[str, Any]) -> None:
    """Persiste el estado de activación de miembros."""
    try:
        os.makedirs("data", exist_ok=True)
        with open(PERSISTENCIA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def cargar_miembros() -> List[Dict[str, Any]]:
    """
    Carga los miembros del hogar combinando defaults con persistencia.
    La persistencia solo afecta el campo 'activo' de cada miembro.
    """
    miembros = [dict(m) for m in MIEMBROS_DEFAULT]
    persistencia = _cargar_persistencia()
    if persistencia:
        estados = persistencia.get("activos", {})
        for miembro in miembros:
            miembro_id = miembro["id"]
            if miembro_id in estados:
                miembro["activo"] = estados[miembro_id]
    return miembros


def get_miembros_activos(miembros: Optional[List[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
    """Retorna solo los miembros activos."""
    if miembros is None:
        miembros = cargar_miembros()
    return [m for m in miembros if m.get("activo", False)]


def get_factor_consumo_total(miembros: Optional[List[Dict[str, Any]]] = None) -> float:
    """Suma de factores de consumo de miembros activos."""
    activos = get_miembros_activos(miembros)
    return sum(m["factor_consumo"] for m in activos)


def get_factor_escalado(miembros: Optional[List[Dict[str, Any]]] = None) -> float:
    """
    Factor de escalado para recetas.

    Ejemplos:
        Julián + Annmar (2.0): 2.0 / 2.0 = 1.0  → cantidades originales
        + Nilsa (2.5):         2.5 / 2.0 = 1.25 → +25%
        Solo Julián (1.0):     1.0 / 2.0 = 0.5  → -50%
    """
    total = get_factor_consumo_total(miembros)
    return total / FACTOR_BASE_REFERENCIA


def get_nombres_activos(miembros: Optional[List[Dict[str, Any]]] = None) -> List[str]:
    """Nombres de los miembros activos."""
    activos = get_miembros_activos(miembros)
    return [m["nombre"] for m in activos]


def get_miembro_por_id(miembro_id: str, miembros: Optional[List[Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]:
    """Busca un miembro por su ID."""
    if miembros is None:
        miembros = cargar_miembros()
    for m in miembros:
        if m["id"] == miembro_id:
            return m
    return None


def set_miembro_activo(miembro_id: str, activo: bool) -> None:
    """
    Activa o desactiva un miembro y persiste el cambio.
    Retorna True si el miembro fue encontrado, False en caso contrario.
    """
    miembros = cargar_miembros()
    encontrado = False
    for m in miembros:
        if m["id"] == miembro_id:
            m["activo"] = activo
            encontrado = True
            break

    if not encontrado:
        return

    estados = {m["id"]: m["activo"] for m in miembros}
    _guardar_persistencia({"activos": estados})


def nilsa_activa() -> bool:
    """Verifica si Nilsa está activa."""
    miembro = get_miembro_por_id("nilsa")
    if miembro is None:
        return False
    return miembro.get("activo", False)


def toggle_nilsa() -> bool:
    """
    Alterna el estado de Nilsa y devuelve el nuevo estado.
    True = activada, False = desactivada.
    """
    estado_actual = nilsa_activa()
    nuevo_estado = not estado_actual
    set_miembro_activo("nilsa", nuevo_estado)
    return nuevo_estado