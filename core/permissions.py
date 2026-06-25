from fastapi import Depends, HTTPException

from core.auth import get_current_user


def admin_only(
    current_user=Depends(get_current_user)
):
    if current_user["role_id"] != 1:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user

def branch_manager_only(
    current_user=Depends(get_current_user)
):
    if current_user["role_id"] != 2:   # Replace 2 with your BM role_id
        raise HTTPException(
            status_code=403,
            detail="Branch Manager access required"
        )

    return current_user