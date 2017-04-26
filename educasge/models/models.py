# -*- coding: utf-8 -*-

from odoo import models, fields, api

class educasge(models.Model):
     _name = 'educasge.educasge'

#cabecera del view, en el form
     photo = fields.Binary("Image", help="Ponga aquí su imagen")
     nombre = fields.Char()
     apellido = fields.Char()
#page informacion personal
     sexo = fields.Selection([('H', 'Hombre'), ('M', 'Mujer')], 'Sexo')
     nacionalidad = fields.Char()
     idioma = fields.Char()
     categoria = fields.Char()
     usuario = fields.Char()
     fechaNacimiento = fields.Date('Cumpleaños')
     telefono = fields.Char()
     direccion = fields.Char()
#page datos academicos
     matricula = fields.Char()
     curso = fields.Char()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#        self.value2 = float(self.value) / 100