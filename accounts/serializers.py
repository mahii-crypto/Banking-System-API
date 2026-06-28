from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, BankAccount, Transaction


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source="customer.full_name",
        read_only=True
    )

    class Meta:
        model = BankAccount
        fields = [
            "id",
            "account_number",
            "account_type",
            "balance",
            "customer",
            "customer_name",
        ]


class TransactionSerializer(serializers.ModelSerializer):

    account_number = serializers.CharField(
        source="account.account_number",
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "transaction_type",
            "amount",
            "created_at",
            "account",
            "account_number",
        ]

    def create(self, validated_data):

        transaction = Transaction.objects.create(**validated_data)

        account = transaction.account

        if transaction.transaction_type == "DEPOSIT":
            account.balance += transaction.amount

        elif transaction.transaction_type == "WITHDRAW":

            if account.balance >= transaction.amount:
                account.balance -= transaction.amount
            else:
                raise serializers.ValidationError(
                    "Insufficient balance."
                )

        account.save()

        return transaction