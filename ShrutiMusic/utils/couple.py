from ShrutiMusic.core.mongo import mongodb

coupledb = {}

async def _get_lovers(cid: int):
    chat_data = coupledb.get(cid, {})
    lovers = chat_data.get("couple", {})
    if not lovers:
        # Try fetching from MongoDB
        try:
            db_data = await mongodb.coupledata.find_one({"chat_id": cid})
            if db_data:
                lovers = db_data.get("couple", {})
                coupledb[cid] = db_data
        except Exception as e:
            print(f"Error fetching from DB: {e}")
    return lovers

async def get_image(cid: int):
    chat_data = coupledb.get(cid, {})
    image = chat_data.get("img", "")
    if not image:
        # Try fetching from MongoDB
        try:
            db_data = await mongodb.coupledata.find_one({"chat_id": cid})
            if db_data:
                image = db_data.get("img", "")
                coupledb[cid] = db_data
        except Exception as e:
            print(f"Error fetching image from DB: {e}")
    return image

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    return lovers.get(date, False)

async def save_couple(cid: int, date: str, couple: dict, img: str):
    # Save in memory
    if cid not in coupledb:
        coupledb[cid] = {"couple": {}, "img": ""}
    coupledb[cid]["couple"][date] = couple
    coupledb[cid]["img"] = img
    
    # Also save in MongoDB for persistence
    try:
        await mongodb.coupledata.update_one(
            {"chat_id": cid},
            {
                "$set": {
                    "chat_id": cid,
                    "couple": {date: couple},
                    "img": img,
                    "updated_at": __import__("datetime").datetime.now()
                }
            },
            upsert=True
        )
        print(f"✅ Couple saved for chat {cid}")
    except Exception as e:
        print(f"❌ Error saving couple to DB: {e}")
