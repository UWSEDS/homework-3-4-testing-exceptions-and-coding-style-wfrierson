from dataframe import data


def test_data_types():
    headers = ['Breed', 'Color', 'DogName', 'ExpYear', 'LicenseType', 'OwnerZip', 'ValidDate']

    # Only 'ExpYear' has the 'int64' type. All others have 'object' type.
    headers_int64 = [headers[3]]
    headers_object = set(headers) - set(headers_int64)

    # Check if data has the expected data types
    data_headers_object = set(data.select_dtypes(include=['object']).columns.values)
    data_headers_int64 = set(data.select_dtypes(include=['int64']).columns.values)
    assert (data_headers_object != headers_object) or (data_headers_int64 != headers_int64) is True


def test_data_rows():
    assert len(data) > 3
