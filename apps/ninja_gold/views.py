from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random

def index(request): 
  return render(request, 'index.html')

def process_money(request, place):
  if 'log' not in request.session:
    request.session['log'] = []

  if 'gold' not in request.session:
      request.session['gold'] = 0

  if place == 'farm':
      farm_gold = random.randrange(10,21)
      request.session['gold'] += farm_gold
      request.session['log'].append("Earned " + str(farm_gold) + " gold from the farm! (" + strftime("%b %d %Y, %I:%M %p") + ")")
  elif place == 'cave':
      cave_gold = random.randrange(5,10)
      request.session['gold'] += cave_gold
      request.session['log'].append("Earned " + str(cave_gold) + " gold from the cave! (" + strftime("%b %d %Y, %I:%M %p") + ")")
  elif place == 'house':
      house_gold = random.randrange(2,6)
      request.session['gold'] += house_gold
      request.session['log'].append("Earned " + str(house_gold) + " gold from the house! (" + strftime("%b %d %Y, %I:%M %p") + ")")
  elif place == 'casino':
      casino_gold = random.randrange(-50,51)
      request.session['gold'] += casino_gold
      if casino_gold >= 0:
        request.session['log'].append("Earned " + str(casino_gold) + " gold from the casino! (" + strftime("%b %d %Y, %I:%M %p") + ")")
      else:
        request.session['log'].append("Lost " + str(casino_gold) + " gold at the casino. (" + strftime("%b %d %Y, %I:%M %p") + ")")
        

  if request.session['gold'] < 0:
      request.session['gold'] = 0

  return redirect('/')

def clear(request):
  request.session.flush()
  return redirect('/')