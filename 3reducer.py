s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0


counter = 0
old_payment_value = None


for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != thisKey:
    # if thisKey:
    #   # output the last key value pair result
    #   #r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = paymentType 
    thisValue = 0.0
  
  # apply the aggregation function
  #thisValue += float(amount)
  if old_payment_value is None:
    old_payment_value = paymentType

  if old_payment_value == paymentType:
    counter = counter + 1
  else:
    r.write(old_payment_value + '\t' + str(counter)+'\n' )
    counter = 1
    old_payment_value = paymentType

# output the final entry when done
r.write(old_payment_value + '\t' + str(counter)+'\n' )

s.close()
r.close()