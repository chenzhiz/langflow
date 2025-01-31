from typing import List

from langflow.custom import Component
from langflow.io import DataInput, Output, TextInput
from langflow.schema import Data


class FilterDataComponent(Component):
    display_name = "Filter Data"
    description = "Filters a Data object based on a list of keys."
    icon = "filter"

    inputs = [
        DataInput(
            name="data",
            display_name="Data",
            info="Data object to filter.",
        ),
        TextInput(
            name="filter_criteria",
            display_name="Filter Criteria",
            info="List of keys to filter by.",
            is_list=True,
        ),
    ]

    outputs = [
        Output(display_name="Filtered Data", name="filtered_data", method="filter_data"),
    ]

    def filter_data(self) -> Data:
        filter_criteria: List[str] = self.filter_criteria
        data = self.data.data if isinstance(self.data, Data) else {}

        # Filter the data
        filtered = {key: value for key, value in data.items() if key in filter_criteria}

        # Create a new Data object with the filtered data
        filtered_data = Data(data=filtered)
        self.status = filtered_data
        return filtered_data
