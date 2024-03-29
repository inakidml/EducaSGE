# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class educasge(models.Model):
    _name = 'educasge.educasge'

    # cabecera del view, en el form
    photo = fields.Binary("Image", help="Ponga aquí su imagen")
    nombre = fields.Char(required="true")
    apellido = fields.Char(required="true")
    dni = fields.Char('DNI', required="true")
    # page informacion personal
    sexo = fields.Selection([('H', 'Hombre'), ('M', 'Mujer')], 'Sexo')
    nacionalidad = fields.Char()
    idioma = fields.Char()
    categoria = fields.Char('Categaría')
    usuario = fields.Char()
    fechaNacimiento = fields.Date('Cumpleaños')
    telefono = fields.Char()
    direccion = fields.Char('Dirección')
    alumnocursoids = fields.One2many('educasge.alumnoscursos', 'educasge_id', 'Notas cursos')


    _sql_constraints = [
        ('unique_dni',
         'unique(dni)',
         'El campo DNI, debe ser unico')
        ]

    @api.one
    @api.constrains('fechaNacimiento')
    def _check_birthdate(self):
        if self.fechaNacimiento > fields.Date.today():
            raise ValidationError(("La fecha de nacimiento no puede ser posterior a la actual!"))


class cursos(models.Model):
    _name = 'educasge.cursos'

    name = fields.Char(string='Nombre', size=32, required=True)
    horas = fields.Char(string='Horas', size=3, required=True)
    descripcion = fields.Char(string='Decripcion', size=500)


class educasgealumnoscursos(models.Model):
    _name = 'educasge.alumnoscursos'

    educasge_id = fields.Many2one('educasge.educasge', 'Alumno', ondelete="cascade")
    cursos_id = fields.Many2one('educasge.cursos', 'Curso')
    nota = fields.Char();

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()

    #     @api.depends('value')
    #     def _value_pc(self):
    #        self.value2 = float(self.value) / 100

    _sql_constraints = [
        ('unique_curso_alummo',
         'UNIQUE(educasge_id, cursos_id)',
         'El alumno solo puede estar inscrito una vez a cada curso')
    ]

