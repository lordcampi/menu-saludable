from html import escape
from pathlib import Path

import streamlit as st


def cargar_estilos():
    """Carga los estilos globales sin mezclar CSS con la lógica de la app."""
    css_path = Path(__file__).with_name("styles.css")
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def encabezado_pagina(eyebrow, titulo, descripcion, chips=None):
    chips_html = "".join(
        f'<span class="app-chip">{escape(str(chip))}</span>'
        for chip in (chips or [])
    )
    st.markdown(
        (
            '<section class="app-hero">'
            f'<p class="app-eyebrow">{escape(eyebrow)}</p>'
            f'<h1>{escape(titulo)}</h1>'
            f'<p class="app-hero-copy">{escape(descripcion)}</p>'
            f'<div class="app-chip-row">{chips_html}</div>'
            "</section>"
        ),
        unsafe_allow_html=True,
    )


def encabezado_seccion(titulo, descripcion=None):
    descripcion_html = (
        f'<p class="app-section-copy">{escape(descripcion)}</p>'
        if descripcion
        else ""
    )
    st.markdown(
        (
            '<div class="app-section-heading">'
            f"<h2>{escape(titulo)}</h2>"
            f"{descripcion_html}"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def callout(texto, etiqueta="Consejo"):
    st.markdown(
        (
            '<div class="app-callout">'
            f'<span class="app-callout-label">{escape(etiqueta)}</span>'
            f"<p>{escape(texto)}</p>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )
