from typing import Any, Dict


def paginate(query, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """
    Apply pagination to a SQLAlchemy query.

    Args:
        query: SQLAlchemy query object
        page: current page number
        page_size: number of records per page

    Returns:
        dictionary with paginated results
    """

    if page < 1:
        page = 1

    offset = (page - 1) * page_size

    total = query.count()

    items = query.limit(page_size).offset(offset).all()

    return {
        "page": page,
        "page_size": page_size,
        "total_records": total,
        "total_pages": (total + page_size - 1) // page_size,
        "data": items
    }
