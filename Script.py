def ground_shipping(weight):

  if weight > 10 :
    cost = weight * 4.75 + 20

  elif weight >= 6 and weight < 10:
    cost = weight * 4 + 20

  elif weight >= 2 and weight < 6:
    cost = weight * 3 + 20

  else:
    cost = weight * 1.50 + 20

  return cost
  

def drone_shipping(weight):
  if weight > 10 :
    cost = weight * 14.25
    return cost
  elif weight >= 6 and weight <10:
    cost = weight * 12
    return cost
  elif weight >= 2 and weight < 6:
    cost = weight * 9
    return cost
  else:
    cost = weight * 4.50 
    return cost


def cheaper_offer(weight):
  ground=ground_shipping(weight)
  premium_ground_shipping=125
  drone=drone_shipping(weight)

  if ground < premium_ground_shipping and ground < drone:
    print("The cheapest method you can use is ground delivery. It costs $"+str(ground))
  elif drone < premium_ground_shipping and drone < ground:
    print("The cheapest method you can use is drone delivery. It costs $"+str(drone))
  else:
    print("The cheapest method you can use is ground delivery. It costs $"+str(premium_ground_shipping))

cheaper_offer(41.5)
