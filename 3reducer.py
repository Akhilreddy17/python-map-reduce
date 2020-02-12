s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0


count = 0
valueofoldpayment = None


for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != thisKey:
    

    # start over when changing keys
    thisKey = paymentType 
    thisValue = 0.0
  
  # apply the aggregation function
 
  if valueofoldpayment is None:
    valueofoldpayment = paymentType

  if valueofoldpayment == paymentType:
    count = count + 1
  else:
    r.write(valueofoldpayment + '\t' + str(count)+'\n' )
    count = 1
    valueofoldpayment = paymentType

# output the final entry when done
r.write(valueofoldpayment + '\t' + str(count)+'\n' )

s.close()
r.close()