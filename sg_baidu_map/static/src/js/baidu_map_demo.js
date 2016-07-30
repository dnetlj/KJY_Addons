openerp.sg_baidu_map = function(instance, local) {
    var QWeb = instance.web.qweb;
//    var session = instance.web.session;

    local.baidu_map_demo = instance.Widget.extend({
        template: 'baidu_map',

        start: function () {
            this._super();
            this.$el.append($(QWeb.render("baidu_map",{})));
            this.display_map();
        },

//            return new instance.web.Model('toproerp.noticecategory')
//                .query(['id','name'])
//                .all()
//                .then(function (results) {
//                 _.each(results, function(result) {
//                return new instance.web.Model('toproerp.notice')
//                .call("searchbycate_method",[result.name])
//                .then(function(results){
//                     self.$el.append($(QWeb.render("categary",{item: result,noticelist:results})));
//             })
//             })


        display_map: function () {
            //var self = this;
            // 百度地图API功能
            self.map = new BMap.Map("allmap");    // 创建Map实例
            var point = new BMap.Point(116.404, 39.915);  // 创建点坐标
            map.centerAndZoom(point, 15);
            //map.centerAndZoom(new BMap.Point(116.404, 39.915), 11);  // 初始化地图,设置中心点坐标和地图级别
            map.addControl(new BMap.MapTypeControl());   //添加地图类型控件
            map.setCurrentCity("北京");          // 设置地图显示的城市 此项是必须设置的
            map.enableScrollWheelZoom(true);
        },

        });

    instance.web.client_actions.add('baidu_map_demo', 'instance.sg_baidu_map.baidu_map_demo');

//this.trigger('client_ready', false);

 }


