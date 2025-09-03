SELECT
`incident_id`,
`plan_id`,
`plan_notification_id`,
max(`count`) as `count`,
`max`,
`age`,
`wait`,
`step`,
`current_step`,
`step_count`
FROM (
    SELECT
        `message`.`incident_id` as `incident_id`,
        `message`.`plan_notification_id` as `plan_notification_id`,
        count(`message`.`id`) as `count`,
        `plan_notification`.`repeat` + 1 as `max`,
        TIMESTAMPDIFF(SECOND, max(`message`.`created`), NOW()) as `age`,
        `plan_notification`.`wait` as `wait`,
        `plan_notification`.`step` as `step`,
        `incident`.`current_step`,
        ANY_VALUE(`plan`.`step_count`) as `step_count`,
        ANY_VALUE(`message`.`plan_id`) as `plan_id`,
        ANY_VALUE(`message`.`application_id`) as `application_id`,
        `incident`.`context`
    FROM `message`
    JOIN `incident` ON `message`.`incident_id` = `incident`.`id`
    JOIN `plan_notification` ON `message`.`plan_notification_id` = `plan_notification`.`id`
    JOIN `plan` ON `message`.`plan_id` = `plan`.`id`
    WHERE `incident`.`active` = 1
    GROUP BY `incident`.`id`, `message`.`plan_notification_id`, `message`.`target_id`
) as `inner`
GROUP BY `incident_id`, `plan_notification_id`, `step_count`
HAVING `age` > `wait` AND (`count` < `max`
                           OR (`count` = `max` AND `step` = `current_step`
                               AND `step` < `step_count`));