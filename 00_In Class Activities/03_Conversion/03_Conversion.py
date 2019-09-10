# Author: Nate K
# Date of Creation: 09/10/2019
# Date of Last Edit: 09/10/2019
# Conversion from Miles to Lightyears
# Source for light years to KM conversion: http://www.kylesconverter.com/length/miles-to-light-years

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/10/2019

import locale
locale.setlocale(locale.LC_ALL, 'en_US')

UR_dist = float(input("How many light years would you like to convert to miles?\n\n"))

dist_KM = UR_dist * (9.4607304725808*(10**15)) # conversion from light years to km
dist_MI = dist_KM / 1.609 # conversion from km to miles, sourced from Google.com
print("\n\n",UR_dist, "light years is around", int(dist_MI), "in miles\n\n\n")