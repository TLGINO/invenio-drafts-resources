"""Example of a record model."""

from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)


class ParentRecordMetadata(db.Model, RecordMetadataBase):
    """Model for mock module metadata."""

    __tablename__ = "parent_mock_metadata"


class DraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for mock module metadata."""

    __tablename__ = "draft_mock_metadata"
    __parent_record_model__ = ParentRecordMetadata


class RecordMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for mock module metadata."""

    __tablename__ = "record_mock_metadata"
    __parent_record_model__ = ParentRecordMetadata


class ParentState(db.Model, ParentRecordStateMixin):
    """Model for mock module for parent state."""

    __parent_record_model__ = ParentRecordMetadata
    __record_model__ = RecordMetadata
    __draft_model__ = DraftMetadata


class FileRecordMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for mock module record files."""

    __record_model_cls__ = RecordMetadata

    __tablename__ = "mock_record_files"


class FileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for mock module draft files."""

    __record_model_cls__ = DraftMetadata

    __tablename__ = "mock_draft_files"
