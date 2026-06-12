import frappe


def execute(filters=None):

    filters = filters or {}

    columns = [
        {
            "label": "Member Name",
            "fieldname": "full_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Email",
            "fieldname": "email",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": "Email Domain",
            "fieldname": "domain",
            "fieldtype": "Data",
            "width": 180
        }
    ]

    # ----------------------------
    # Member Filter
    # ----------------------------

    member_filters = {}

    if filters.get("member"):
        member_filters["name"] = filters.get("member")

    members = frappe.get_all(
        "Library Member",
        filters=member_filters,
        fields=[
            "full_name",
            "email"
        ]
    )

    data = []

    domain_count = {}

    gmail_count = 0
    other_count = 0

    # ----------------------------
    # Process Data
    # ----------------------------

    for member in members:

        domain = ""

        if member.email:
            domain = member.email.split("@")[-1]

        # Domain Filter
        if filters.get("domain"):

            if domain.lower() != filters.get("domain").lower():
                continue

        # Domain Count
        domain_count[domain] = (
            domain_count.get(domain, 0) + 1
        )

        # KPI Count
        if domain == "gmail.com":
            gmail_count += 1
        else:
            other_count += 1

        data.append({
            "full_name": member.full_name,
            "email": member.email,
            "domain": domain
        })

    # ----------------------------
    # Summary Cards
    # ----------------------------

    summary = [
        {
            "value": len(data),
            "label": "Total Members",
            "datatype": "Int",
            "indicator": "Blue"
        },
        {
            "value": len(domain_count),
            "label": "Unique Domains",
            "datatype": "Int",
            "indicator": "Green"
        },
        {
            "value": gmail_count,
            "label": "Gmail Users",
            "datatype": "Int",
            "indicator": "Blue"
        },
        {
            "value": other_count,
            "label": "Other Domains",
            "datatype": "Int",
            "indicator": "Orange"
        }
    ]

    # ----------------------------
    # Chart
    # ----------------------------

    chart = {
        "data": {
            "labels": list(domain_count.keys()),
            "datasets": [
                {
                    "name": "Members",
                    "values": list(domain_count.values())
                }
            ]
        },
        "type": "pie",
        "colors": [
            "#4F8EF7",
            "#6BCB77",
            "#FFD93D",
            "#FF6B6B"
        ]
    }

    # ----------------------------
    # Message
    # ----------------------------

    message = f"""
        Total Members: <b>{len(data)}</b><br>
        Gmail Users: <b>{gmail_count}</b><br>
        Other Domain Users: <b>{other_count}</b>
    """

    return columns, data, message, chart, summary