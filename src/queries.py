class Queries:
    cp_subscribers_last7days = """
        SELECT
            display_name AS name,
            email_address AS email
        FROM m_client
        WHERE email_address NOT LIKE '%@boomcredit%'
        AND email_address NOT LIKE '%@braspay%'
        AND email_address LIKE '%@%.%'
        AND created_date >= DATE(NOW()) - INTERVAL 1 DAY
        GROUP BY email;
    """
