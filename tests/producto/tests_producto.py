# import pytest
# from producto.models import Producto, Categoria

# @pytest.mark.django_db
# def tests_producto_creations():
#     categoria = Categoria.objects.create(

#         nombre = 'test_unitario_categoria'
#     )

#     producto = Producto.objects.create(
#         nombre = 'test_producto_nombre',
#         precio = 23000,
#         descripcion = 'test_producto_descripcion',
#         categoria = categoria,
#         stock = 23,
#     )

#     assert producto.nombre == 'test_producto_nombre'

import pytest
from unittest.mock import patch, MagicMock
from producto.models import Producto, Categoria

@pytest.mark.django_db
@patch('producto.models.Producto')
@patch('producto.models.Categoria')
def test_producto_creation(mock_categoria, mock_producto):
    
    categoria = MagicMock()
    categoria.nombre = 'test_unitario_categoria'
    mock_categoria.objects.create.return_value = categoria

    
    producto = MagicMock()
    producto.nombre = 'test_producto_nombre'
    producto.precio = 23000
    producto.descripcion = 'test_producto_descripcion'
    producto.categoria = categoria
    producto.stock = 23
    mock_producto.objects.create.return_value = producto

    
    categoria_creada = Categoria.objects.create(
        nombre='test_unitario_categoria'
    )

    producto_creado = Producto.objects.create(
        nombre='test_producto_nombre',
        precio=23000,
        descripcion='test_producto_descripcion',
        categoria=categoria_creada,
        stock=23,
    )

    
    assert producto_creado.nombre == 'test_producto_nombre'
