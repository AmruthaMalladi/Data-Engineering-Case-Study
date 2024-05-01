-- assuming conversion flag column, which confirms if it was converted or now. 
CREATE OR REPLACE VIEW campaign_performance AS
SELECT
    i.ad_campaign_id,
    i.user_id,
    COUNT(i.impression_id) AS total_impressions,
    COUNT(c.click_id) AS total_clicks,
    SUM(c.conversion_flag) AS total_conversions,
    CASE WHEN COUNT(i.impression_id) > 0 THEN
        ROUND((COUNT(c.click_id) * 100.0) / COUNT(i.impression_id), 2)
    ELSE 0 END AS click_through_rate,
    CASE WHEN COUNT(c.click_id) > 0 THEN
        ROUND((SUM(c.conversion_flag) * 100.0) / COUNT(c.click_id), 2)
    ELSE 0 END AS conversion_rate
FROM
    ad_impressions i
LEFT JOIN
    clicks_and_conversions c ON i.user_id = c.user_id AND i.ad_campaign_id = c.ad_campaign_id
GROUP BY
    i.ad_campaign_id, i.user_id;
