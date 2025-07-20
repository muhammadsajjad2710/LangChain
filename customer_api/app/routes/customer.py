from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DNISTable
from app.schemas import TransferRequest, HandoffRequest
from app.auth import verify_token

router = APIRouter()

@router.post("/get_transfer_number_and_lock_row")
def get_transfer_number_and_lock_row(request: TransferRequest, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    row = db.query(DNISTable).filter(DNISTable.locked == False).first()
    if row:
        row.engagementId = request.engagementId
        row.details = request.details
        row.locked = True
        db.commit()
        return {"zoom_phone_ar_number": row.zoom_phone_ar_number}
    raise HTTPException(status_code=404, detail="No available rows")

@router.post("/get_call_details_and_free_row")
def get_call_details_and_free_row(poly_num_to_call: str, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    row = db.query(DNISTable).filter(DNISTable.poly_num_to_call == poly_num_to_call).first()
    if row:
        row.locked = False
        db.commit()
        return {"engagementId": row.engagementId, "details": row.details}
    raise HTTPException(status_code=404, detail="Call details not found")

@router.post("/handoff")
def handoff(request: HandoffRequest, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    row = db.query(DNISTable).filter(DNISTable.engagementId == request.shared_id).first()
    if row:
        return {"details": row.details}
    raise HTTPException(status_code=404, detail="Handoff details not found")
