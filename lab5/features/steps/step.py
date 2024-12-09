from behave import given, when, then, step
from lab4 import field
@given('a list of goods')
def step_given_list_of_goods(context):
    context.goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

@when('extract the title field')
def step_when_extract_title(context):
    context.result = list(field(context.goods, 'title'))

@then('a list')
def step_then_result_titles(context):
    assert context.result == ['Ковер', 'Диван для отдыха']

@when('extract the title and price fields')
def step_when_extract_title(context):
    context.result = list(field(context.goods, 'title','price'))

@then('a list of goods with title and price')
def step_then_result_titles(context):
    expected = [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]
    assert context.result == expected


@when('extract a non-existent field')
def step_when_extract_title(context):
    context.result = list(field(context.goods, 'qwerty'))


@then('an empty list')
def step_then_result_titles(context):
    assert context.result == []


@when('extract the title, price, color fields')
def step_when_extract_title(context):
    context.result = list(field(context.goods, 'title','price','color'))

@then('a list of goods with title, price, color')
def step_then_result_titles(context):
    expected = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    assert context.result == expected
