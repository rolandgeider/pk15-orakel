# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django import template
from django.forms.widgets import CheckboxInput, ClearableFileInput
from django.forms import RadioSelect

register = template.Library()


@register.inclusion_tag('tags/osm_coordinate.html')
def osm_coordinate(lat, lon):
    '''
    Renders the coordinate on an openstreetmap map
    '''

    return {'lat': lat,
            'lon': lon}

@register.inclusion_tag('tags/coordinate.html')
def coordinate(lat, lon):
    '''
    Renders the coordinate
    '''

    return {'lat': lat,
            'lon': lon}


@register.filter(name='DMS')
def DMS(coord):
    coord = float(coord)
    deg = int(coord)
    min = int((coord - deg) * 60)
    sec = ((coord - deg)*60 - min) * 60
    return "%d° %d' %.2f''" % (deg, min, sec)

@register.filter(name="float")
def to_float(value):
    return float(value)

#
# Form utils
#
@register.filter(name='form_field_add_css')
def form_field_add_css(field, css):
    '''
    Adds a CSS class to a form field. This is needed among other places for
    bootstrap 3, which needs a 'form-control' class in the field itself
    '''
    return field.as_widget(attrs={"class": css})


@register.filter(name='is_checkbox')
def is_checkbox(field):
    '''
    Tests if a field element is a checkbox, as it needs to be handled slightly different

    :param field: a form field
    :return: boolen
    '''
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name='is_fileupload')
def is_fileupload(field):
    '''
    Tests if a field element is a file upload, as it needs to be handled slightly different

    :param field: a form field
    :return: boolen
    '''
    return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__

@register.filter(name="is_radio")
def is_radio(field):
    return 'radio' in field.field.widget.__class__.__name__.lower()
    return isinstance(field.field.widget, RadioSelect)

@register.inclusion_tag('tags/render_form_element.html')
def render_form_field(field):
    '''
    Renders a form field with all necessary labels, help texts and labels
    within 'form-group'.

    See bootstrap documentation for details: http://getbootstrap.com/css/#forms
    '''

    return {'field': field}


@register.inclusion_tag('tags/render_form_submit.html')
def render_form_submit(save_text='Save', button_class='default'):
    """
    Comfort function that renders a submit button with all necessary HTML
    and CSS

    :param save_text: the text to use on the submit button
    :param button_class: CSS class to apply to the button, default 'default'
    """
    if button_class in ('default',
                        'primary',
                        'success',
                        'info',
                        'warning',
                        'danger',
                        'link'):
        button_class = button_class
    else:
        button_class = 'default'

    return {'save_text': save_text,
            'button_class': button_class}


@register.inclusion_tag('tags/render_form_errors.html')
def render_form_errors(form):
    """
    Renders the non-field errors of a form with all necessary HTML and CSS
    (non-field errors refer to errors that can't be associated to any single
    field)

    :param form: the form object
    """
    return {'form': form}


@register.inclusion_tag('tags/render_form_fields.html')
def render_form_fields(form, submit_text='Save', show_save=True):
    '''
    Comfort function that renders all fields in a form, as well as the submit
    button

    Internally it simply calls the other table_form_* functions and will render
    the fields in the order they were defined. If you want to change this, you
    need to call table_form_field for each field yourself. This function will
    also render a hidden field with a CSRF token, so be sure to pass it to the
    template.

    It is still necessary to enclose its output in <form> tags!

    :param form: the form to be rendered
    :param save_text: the text to use on the submit button
    '''

    return {'form': form,
            'show_save': show_save,
            'submit_text': submit_text}
