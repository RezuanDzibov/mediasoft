import uuid

from sqlalchemy import Column, ForeignKey, String, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class UUIDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class City(UUIDMixin, Base):
    __tablename__ = "cities"

    name = Column(String)
    streets = relationship("Street", back_populates="city")


class Street(UUIDMixin, Base):
    __tablename__ = "streets"

    name = Column(String)
    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"))
    city = relationship("City", back_populates="streets")
    shops = relationship("Shop", back_populates="street")


class Shop(UUIDMixin, Base):
    __tablename__ = "shops"

    name = Column(String)
    building = Column(String)
    open_time = Column(Time)
    close_time = Column(Time)
    street_id = Column(UUID(as_uuid=True), ForeignKey("streets.id"))
    street = relationship("Street", back_populates="shops")
