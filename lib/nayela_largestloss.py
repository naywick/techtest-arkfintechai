from unittest import TestCase

def largest_loss(pricesLst):
    largest_loss = 0

    if len(pricesLst) < 2:
        return largest_loss

    for i in range(1, len(pricesLst)):
        calculating_loss = (pricesLst[x] - pricesLst[x-1])
        if calculating_loss > largest_loss:
            largest_loss = calculating_loss
    return largest_loss


### Old, poorly indented code ###
# def largest_loss(pricesLst):
#   largest_loss = 0

#  if len(pricesLst) < 2:
#  return largest loss

#   for i in range(1, len(pricesLst)):
#     calculating_loss = (pricesLst[x] - pricesLst[x-1])
#     if calculating_loss > largest_loss:
#       largest_loss = calculating_loss
#     return largest_loss
