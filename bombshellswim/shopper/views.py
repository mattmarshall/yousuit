from django.shortcuts import render
from django.utils import simplejson as json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def default_shopper():
	ret = dict()
	ret['1a'] = { 'weight': '110', 'inches': '64', 'build': 'petite' }
	ret['1b'] = { 'shoulders': 'narrow', 'bust': 'average', 'torso': 'average', 'waist': 'average', 'hips': 'average'}
	ret['2a'] = { 'priority': 'accentuate', 'activity': 'tanning', 'style': 'flirty'}
	ret['3a'] = { 'shoulders': 'braoden', 'bust': 'accentuate', 'torso': 'shorten', 'waist': 'contain', 'hips': 'minimize'}
	return ret

def customize(request, step):
	context = { 'step' : step, 'shopper': request.session.get('shopper') }
	return render(request, 'step.html', context)

def substep(request, substep):
	context = { 'shopper': request.session.get('shopper') }
	return render(request, 'step%s.html' % substep, context)                                       

@csrf_exempt
def set_value(request):
    val = request.session.get('shopper')
    if val is None:
        request.session['shopper'] = default_shopper()
        val = request.session.get('shopper')
    save = json.loads(request.body)
    (step, key, value) = (save['step'], save['section'], save['value'])
    print '%s %s %s' % (step, key, value)
    val[step][key] = value
    request.session.modified = True
    data = json.dumps({'success': True, 'saved': val})
    return HttpResponse(data, content_type='application/json')