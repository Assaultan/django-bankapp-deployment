from basicapp.models import Customers,Transfers
from basicapp.api.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
 
@api_view(['GET','PUT','DELETE'])
def customer_detail(request,pk):
    
    if request.method=='GET':
        try: 
            customer = Customers.objects.get(pk=pk)
        except:
            return Response({'error':'Customer not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='PUT':
        customer = Customers.objects.get(pk=pk)
        serializer = CustomerSerializer(customer,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        customer = Customers.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)