from medical_problems import get_medical_problems_sorted

def test_medical_problems_sorted():
    result = get_medical_problems_sorted(r"/Users/utkarshmishra/Documents/python-automotive-batch9/medical/patient.xml")

    expected = [
        "Allergy",
        "Fracture",
        "Migraine",
        "Sinus",
        "Thyroid"
    ]

    assert result == expected