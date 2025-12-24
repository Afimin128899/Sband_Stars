from utils.db import add_ref

def process_referral(ref_id, new_user_id):
    if ref_id != new_user_id:
        add_ref(ref_id)