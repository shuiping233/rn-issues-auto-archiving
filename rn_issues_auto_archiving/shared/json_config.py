

from dataclasses import dataclass
from typing import TypedDict, TypeAlias

IssueType: TypeAlias = str


class ConfigJson(TypedDict):
    class ArchivedDocument(TypedDict):
        class ProcessingAction(TypedDict):
            add_prefix: str
            add_suffix: str
            remove_keyword: list[str]

        rjust_space_width: int
        rjust_character: str
        table_separator: str
        archive_template: str
        action_name_map: dict[str, str]
        issue_title_processing_rules: dict[IssueType,
                                           ProcessingAction]
        reopen_workflow_prefix_map: dict[str, str]

    class IssueType(TypedDict):
        type_keyword: dict[str, str]
        need_introduced_version_issue_type: list[str]
        label_map: dict[str, str]

    version_regex: str
    introduced_version_reges: list[str]
    issue_type: IssueType
    archived_version_reges_for_comments: list[str]
    archive_necessary_labels: list[str]
    archived_document: ArchivedDocument


@dataclass
class Config():
    @dataclass
    class IssueType():
        type_keyword: dict[str, str] = {}
        need_introduced_version_issue_type: list[str] = []
        label_map: dict[str, str] = {}

    @dataclass
    class ArchivedDocument():
        @dataclass
        class ProcessingAction(TypedDict):
            add_prefix: str = str()
            add_suffix: str = str()
            remove_keyword: list[str] = []

        rjust_space_width: int = 0
        rjust_character: str = str()
        table_separator: str = str()
        archive_template: str = str()
        action_name_map: dict[str, str] = {}
        issue_title_processing_rules: dict[IssueType,
                                           ProcessingAction] = {}
        reopen_workflow_prefix_map: dict[str, str] = {}

    # 从env读取
    token: str = str()
    output_path: str = str()

    # 从命令行参数读取
    config_path: str = str()
    test_platform_type: str | None = None

    # 从配置文件json读取
    archive_necessary_labels: list[str] = []
    archived_version_reges_for_comments: list[str] = []
    version_regex: str = str()
    issue_type: IssueType = IssueType()
    introduced_version_reges: list[str] = []
    archived_document: ArchivedDocument = ArchivedDocument()