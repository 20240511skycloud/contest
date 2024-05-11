from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int(attribute='id', data_key='id') # 设置 'id' 字段的别名为 'id'
    c_user_id = fields.Int(attribute="c_user_id", data_key="c_user_id")
    c_title = fields.Str(attribute='c_title', data_key='title')
    c_description = fields.Str(attribute='c_description', data_key='description')
    c_status = fields.Str(attribute='c_status', data_key='status')

