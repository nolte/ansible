import pytest


from ansible.modules.cloud.misc.terraform import convertPythonVarValueToTerraformVarCommandlineParameter

testdata = [
    ("1",'"1"'),
    (1,'"1"'),
    ([1],'["1"]'),
    ([1,2,3],'["1","2","3"]'),
    (["1","2","3"],'["1","2","3"]'),
    ({'content': 'myExample' },'{ content = "myExample" }'),
    ({'content': 'myExample', 'target_name': '/tmp/test.txt' },'{ content = "myExample", target_name = "/tmp/test.txt" }')
]


@pytest.mark.parametrize("varValue,expected", testdata)
def test_timedistance_v0(varValue, expected):
    assert expected == convertPythonVarValueToTerraformVarCommandlineParameter(varValue)
