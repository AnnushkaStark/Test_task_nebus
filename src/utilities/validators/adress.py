from schemas.address import AddressCreate


async def validate(schema: AddressCreate) -> AddressCreate:
    if schema.home_number <= 0:
        raise Exception("The house number must be greater than 0")
    if schema.room_number <= 0:
        raise Exception("The room number must be greater than 0")
    if 0 < int(schema.latitude) > 90:
        raise Exception("The latitude should be between 0 and 90 degrees")
    if 0 < int(schema.longitude) > 180:
        raise Exception("The longitude must be between 0 and 180 degrees")
    return schema
