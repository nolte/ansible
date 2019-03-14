import pytest


def convertPythonVarValueToTerraformVarCommandlineParameter(varValue):
    if(isinstance(varValue, list)):
        varstring = ""
        listVars = []
        for index,val in enumerate(varValue):
            varstring = varstring + formatSimpleValue(val)

            if index < (len(varValue) -1):
                varstring = varstring + ","

        return "["+varstring+"]"
    elif(isinstance(varValue, dict)):
        varstring = ""
        i = 0
        for k, v in varValue.items():
            varstring = varstring +  k + " = " + formatSimpleValue(v)
            if i < (len(varValue) -1):
                varstring = varstring + ", "
            i = i + 1

        return "{ "+varstring+" }"
    else:
        return formatSimpleValue(varValue)

def formatSimpleValue(singleValue):
    return '\"'+str(singleValue)+'\"'

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
