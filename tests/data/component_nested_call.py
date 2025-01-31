from random import randint

from langflow.custom import Component
from langflow.inputs.inputs import IntInput, TextInput
from langflow.template.field.base import Output


class MultipleOutputsComponent(Component):
    inputs = [
        TextInput(display_name="Input", name="input"),
        IntInput(display_name="Number", name="number"),
    ]
    outputs = [
        Output(display_name="Certain Output", name="certain_output", method="certain_output"),
        Output(display_name="Other Output", name="other_output", method="other_output"),
    ]

    def certain_output(self) -> int:
        return randint(0, self.number)

    def other_output(self) -> int:
        return self.certain_output()
