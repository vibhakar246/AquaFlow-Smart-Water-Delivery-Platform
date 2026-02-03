#!/bin/bash

echo "🔍 Running Integration Tests for AquaFlow"

# Test 1: Health Check
echo "1. Testing Health Endpoint..."
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:5000/api/health

# Test 2: Order Processing
echo -e "\n2. Testing Order Processing..."
curl -X POST http://localhost:5000/api/order \
  -H "Content-Type: application/json" \
  -d '{"message": "2 x 20L, 1 x 10L"}' \
  -w "\nHTTP Status: %{http_code}\n"

# Test 3: Invalid Order
echo -e "\n3. Testing Invalid Order..."
curl -X POST http://localhost:5000/api/order \
  -H "Content-Type: application/json" \
  -d '{"message": "invalid order"}' \
  -w "\nHTTP Status: %{http_code}\n"

# Test 4: Empty Order
echo -e "\n4. Testing Empty Order..."
curl -X POST http://localhost:5000/api/order \
  -H "Content-Type: application/json" \
  -d '{}' \
  -w "\nHTTP Status: %{http_code}\n"

echo -e "\n✅ Integration tests completed!"
