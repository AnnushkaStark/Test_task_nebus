from sqlalchemy.ext.asyncio import AsyncSession

from schemas.address import AddressCreate
from schemas.organization import OrganizationCreate
from schemas.phone import PhoneCreate
from services import organization as organization_service


async def create_test_organizations(db: AsyncSession) -> None:
    test_organizations = [
        OrganizationCreate(
            name="TestOrg",
            address=AddressCreate(
                country="Россия",
                region="Ленинградская область",
                city="Санкт Петербург",
                street="Коммендантский проспект",
                home_number=1,
                room_number=2,
                latitude=1.00001,
                longitude=2.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204515"),
                PhoneCreate(number="+79062204516"),
            ],
            industry_id=1,
            specializations_ids=[4, 5],
        ),
        OrganizationCreate(
            name="Организация",
            address=AddressCreate(
                country="Россия",
                region="Московская область",
                city="Москва",
                street="Ленина",
                home_number=3,
                room_number=4,
                latitude=2.00001,
                longitude=3.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204517"),
                PhoneCreate(number="+79062204518"),
            ],
            industry_id=1,
            specializations_ids=[5, 6],
        ),
        OrganizationCreate(
            name="Продукты",
            address=AddressCreate(
                country="Россия",
                region="псковская область",
                city="Псков",
                street="Коммуннальная",
                home_number=5,
                room_number=6,
                latitude=4.00001,
                longitude=5.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204519"),
                PhoneCreate(number="+79062204520"),
            ],
            industry_id=1,
            specializations_ids=[4, 6],
        ),
        OrganizationCreate(
            name="Лента",
            address=AddressCreate(
                country="Беларусь",
                region="Минская область",
                city="Минск",
                street="Молодежная",
                home_number=7,
                room_number=8,
                latitude=6.00001,
                longitude=7.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204521"),
                PhoneCreate(number="+79062204522"),
            ],
            industry_id=2,
            specializations_ids=[1, 2],
        ),
        OrganizationCreate(
            name="Одежда",
            address=AddressCreate(
                country="Беларусь",
                region="Брестская область",
                city="Брест",
                street="Победы",
                home_number=9,
                room_number=10,
                latitude=8.00001,
                longitude=9.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204523"),
                PhoneCreate(number="+79062204524"),
            ],
            industry_id=2,
            specializations_ids=[2, 3],
        ),
        OrganizationCreate(
            name="Oзон",
            address=AddressCreate(
                country="Беларусь",
                region="Витебская область",
                city="Витебск",
                street="Победы",
                home_number=9,
                room_number=10,
                latitude=8.00001,
                longitude=9.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204525"),
                PhoneCreate(number="+79062204526"),
            ],
            industry_id=2,
            specializations_ids=[1, 3],
        ),
        OrganizationCreate(
            name="Дизайн",
            address=AddressCreate(
                country="Россия",
                region="Самарская область",
                city="Самара",
                street="Мира",
                home_number=10,
                room_number=11,
                latitude=10.00001,
                longitude=11.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204527"),
                PhoneCreate(number="+79062204528"),
            ],
            industry_id=3,
            specializations_ids=[7, 8],
        ),
        OrganizationCreate(
            name="Креативный хаб",
            address=AddressCreate(
                country="Россия",
                region="Ростовская область",
                city="Ростов",
                street="Нижняя",
                home_number=11,
                room_number=12,
                latitude=12.00001,
                longitude=13.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204529"),
                PhoneCreate(number="+79062204530"),
            ],
            industry_id=3,
            specializations_ids=[8, 9],
        ),
        OrganizationCreate(
            name="Мода",
            address=AddressCreate(
                country="Россия",
                region="Нижегородская область",
                city="Нижний Новгород",
                street="Речная",
                home_number=13,
                room_number=14,
                latitude=14.00001,
                longitude=15.00002,
            ),
            phone_numbers=[
                PhoneCreate(number="+79062204531"),
                PhoneCreate(number="+79062204532"),
            ],
            industry_id=3,
            specializations_ids=[7, 9],
        ),
    ]
    try:
        for schema in test_organizations:
            await organization_service.create(db=db, create_schema=schema)
    except Exception as e:
        raise Exception(str(e))
