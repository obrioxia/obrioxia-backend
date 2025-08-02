# Obrioxia Backend

FastAPI backend for handling Stripe webhook events.

**Live Endpoint:**  
https://obrioxia-backend-1.onrender.com/stripe-webhooks

**Listens to Stripe Events:**
- checkout.session.completed  
- customer.subscription.updated  
- customer.subscription.deleted  
- invoice.payment_succeeded

**Files:**
- `main.py`: FastAPI app  
- `requirements.txt`: Dependencies  
- `render.yaml`: Render deployment config

**Deployment:** Render (Free Tier)  
**Language:** Python 3.13  

Keep `STRIPE_SECRET_KEY` and `STRIPE_SIGNING_SECRET` safe.
