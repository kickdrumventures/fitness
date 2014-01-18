from django.template.defaultfilters import register

@register.filter(name='lookup')
def lookup(dict, key):
	if key in dict:
		return dict[key]
	else:
		return ''