# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class educasge(models.Model):
    _name = 'educasge.educasge'

    # cabecera del view, en el form
    photo = fields.Binary("Image", help="Ponga aquí su imagen")
    nombre = fields.Char(required="true")
    apellido = fields.Char(required="true")
    # page informacion personal
    sexo = fields.Selection([('H', 'Hombre'), ('M', 'Mujer')], 'Sexo')
    nacionalidad = fields.Char()
    idioma = fields.Char()
    categoria = fields.Char('Categaría')
    usuario = fields.Char()
    fechaNacimiento = fields.Date('Cumpleaños')
    telefono = fields.Char()
    direccion = fields.Char('Dirección')
    #alumnoCursoIds = fields.One2many('educasge.alumnoscursos', 'alumno_id', string='Notas cursos')


class cursos(models.Model):
    _name = 'educasge.cursos'

    nombre = fields.Char(string='Nombre', size=32, required=True)
    horas = fields.Char(string='Horas', size=3, required=True)
    descripcion = fields.Char(string='Decripcion', size=500)


class educasgealumnoscursos(models.Model):
    _name = 'educasge.alumnoscursos'
    _description = 'tabla intermedia'

    alumno_id = fields.Many2one('educasge.educasge', string='Alumno', ondelete="cascade")
    cursos_id = fields.Many2one('educasge.cursos', string='Curso')
    nota = fields.char('Nota')

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()

    #     @api.depends('value')
    #     def _value_pc(self):
    #        self.value2 = float(self.value) / 100


    @api.one
    @api.constrains('fechaNacimiento')
    def _check_birthdate(self):
        if self.fechaNacimiento > fields.Date.today():
            raise ValidationError(_("Birth Date can't be greater than current date!"))
