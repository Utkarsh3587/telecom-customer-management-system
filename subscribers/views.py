from datetime import timedelta, datetime

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from subscribers.models import Subscriber
from plans.models import Plan
from customers.models import Customer


class SubscriberCreateListView(ListCreateAPIView):

    def list(self, request, *args, **kwargs):
        # to list all the subscribers
        data = {}
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            data.update({
                'name': subscriber.customer_name,
                'plan': subscriber.plan_name,
                'subscribed_at': subscriber.created_at,
                'expired_at': subscriber.expired_at,
            })
        return Response(data)


    def post(self, request, *args, **kwargs):
        # to create a subsriber
        customer_id = request.data.get('customer_id', '').strip()
        plan_id = request.data.get('plan_id', '').strip()
        customer = Customer.objects.filter(id=customer_id).first()

        if not customer:
            return Response(
                {"message": "Customer does not exist"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        plan = Plan.objects.filter(id=plan_id).first()
        if not plan:
            return Response(
                {"message": "Plan does not exist"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        subscriber = Subscriber.objects.create(
            customer=customer, plan=plan, expired_at=datetime.now() + timedelta(days=plan.validity)
        )
        return Response(
                {"message": "subscribed successfully"}, 
                status=status.HTTP_200_OK
        )


class SubscriberDetailView(RetrieveUpdateDestroyAPIView):

    def set_subscriber(self):
        subscriber_id = str(self.kwargs.get('pk', '')).strip()
        return Subscriber.objects.filter(id=subscriber_id).first()

    def put(self, request, *args, **kwargs):
        """
        to update the plan of a subscriber based on the subscription_type flag
        # subscription_type can be renew or change
        renew - it renews the existing plan
        change - it upgrades or downgrades the existing plan.
        """
        subscriber = self.set_subscriber()

        if subscriber is None:
            return Response(
                {"message": "Subscriber does not exist"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # check for renewal or change of subscription plan
        subscription_type = request.data.get('subscription_type', '').strip()

        if subscription_type not in ['renew', 'change']:
            return Response(
                {"message": "choose either to renew or change plan"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        new_plan = subscriber.plan
        if subscription_type == 'renew':
            plan = Plan.objects.filter(plan_id=subscriber.plan_id).first()

            if not all([plan, plan.status]): return Response(
                {"message": "plan not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            old_plan_name, new_plan_name = request.data('old_plan_name'), request.data('new_plan_name')
            old_plan = Plan.objects.filter(plan__name=old_plan_name).first()
            new_plan = Plan.objects.filter(plan__name=new_plan_name).first()

            if not all([old_plan, new_plan]): return Response(
                {"message": "plan not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        subscriber.plan = new_plan
        subscriber.expired_at=datetime.now() + timedelta(days=new_plan.validity)
        subscriber.save()
        return Response({"message":"plan updated sucessfully"})
