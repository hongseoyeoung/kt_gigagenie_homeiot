/*!     
        jquery.responsiveGallery.js
        v 1.0
        David
        http://www.CodingSerf.com
*/

;(function($){
    $.fn.responsiveGallery = function(option){
		var opts = $.extend({}, $.fn.responsiveGallery.defaults, option), //配置选项
			$rgWrapper = this,
			$rgItems = $rgWrapper.find('li'), //.responsiveGallery-item
			rgItemsLength = $rgItems.length,
			support3d = Modernizr.csstransforms3d, 
			support2d = Modernizr.csstransforms,
			rgCurrentIndex = 0;

			
			rgShowCount = 5,
			rgTansCSS = [],
			animatDuration = opts.animatDuration,
			isAnimating = false,
			touchX = 0;

		function getTransform3dCSS(tx,ty,ry,zIndex,opacity,visibility){
			return {
				'-webkit-transform'	: 'translateX('+tx+') translateZ('+ty+'px) rotateY('+ry+'deg)',
				'-moz-transform'	: 'translateX('+tx+') translateZ('+ty+'px) rotateY('+ry+'deg)',
				'-o-transform'		: 'translateX('+tx+') translateZ('+ty+'px) rotateY('+ry+'deg)',
				'-ms-transform'		: 'translateX('+tx+') translateZ('+ty+'px) rotateY('+ry+'deg)',
				'transform'			: 'translateX('+tx+') translateZ('+ty+'px) rotateY('+ry+'deg)',
				'z-index'			: zIndex,
				'opacity'			: opacity,
				'visibility'		: visibility
			};
		}

		function getTransform2dCSS(t,s,originX,originY,opacity,visibility){
			return {
				'-webkit-transform'	: 'translate('+t+') scale('+s+')',
				'-moz-transform'	: 'translate('+t+') scale('+s+')',
				'-o-transform'		: 'translate('+t+') scale('+s+')',
				'-ms-transform'		: 'translate('+t+') scale('+s+')',
				'transform'			: 'translate('+t+') scale('+s+')',

				'-webkit-transform-origin'	: originX+' '+originY,
				'-moz-transform-origin'		: originX+' '+originY,
				'-ms-transform-origin'		: originX+' '+originY,
				'-o-transform-origin'		: originX+' '+originY,
				'transform-origin'			: originX+' '+originY,

				'opacity'			: opacity,
				'visibility'		: visibility
			};
		}

		function getTransitionCSS(time,ease){
			return {
				'-webkit-transition': 'all '+time+'s '+ease,
				'-moz-transition': 'all '+time+'s '+ease,
				'-ms-transition': 'all '+time+'s '+ease,
				'-o-transition': 'all '+time+'s '+ease,
				'transition': 'all '+time+'s '+ease,
			}
		}

		function getTransform3CSS(){
			var cssArray;

			if(support3d){
				cssArray = [
					// getTransform3dCSS('-100%',	-400, 	45,		0,	0,	'hidden'),

					// getTransform3dCSS('-27.5%', -300, 	45,		1,	1,	'visible'),
					// getTransform3dCSS('12.5%', 	0, 		0,		2,	1,	'visible'),
					// getTransform3dCSS('62.5%', 	-300, 	-45,	1,	1,	'visible'),

					// getTransform3dCSS('300%', 	-400, 	-45,	0,	0,	'hidden')
					getTransform3dCSS('0%',		-400, 	0,		-1,	0,	'hidden'),

					getTransform3dCSS('-37.5%',	-500, 	5,		0,	1,	'visible'),
					getTransform3dCSS('-12.5%',	-200, 	5,		1,	1,	'visible'),
					getTransform3dCSS('12.5%', 	0, 		0,		2,	1,	'visible'),
					getTransform3dCSS('37.5%', 	-200, 	-5,		1,	1,	'visible'),
					getTransform3dCSS('62.5%', 	-500, 	-5,		0,	1,	'visible'),

					getTransform3dCSS('160%', 	-400, 	0,		-1,	0,	'hidden')
				];
			} else if(support2d){
				cssArray = [
					getTransform2dCSS('-100%',	0.65,	'100%',		'50%',	0,	'hidden'),

					getTransform2dCSS('37.5%',	0.8,	'50%',		'50%',	1,	'visible'),
					getTransform2dCSS('12.5%', 	1,		'50%',		'50%',	1,	'visible'),
					getTransform2dCSS('62.5%', 	0.8,	'50%',		'50%',	1,	'visible'),

					getTransform2dCSS('300%', 	0.65,	'0%',		'50%',	0,	'hidden')
				];
			}

			return cssArray;
		}

		function setSectionItems(fun){
			var $items = [];

			$items[0] = $rgItems.eq(rgCurrentIndex-1);
			fun(0,$items[0]);
			for (var i=1;i<=rgShowCount+1;i++) {
				var next = rgCurrentIndex+i-1;
				if(next>=rgItemsLength){
					next = next - rgItemsLength;
				}
				$items[i] = $rgItems.eq(next);
				fun(i,$items[i]);
			}
		}

		function moveGallery(direction){
			isAnimating = true;

			rgCurrentIndex = direction + rgCurrentIndex;
			if(rgCurrentIndex < 0){
				rgCurrentIndex = rgItemsLength - 1;
			}
			if(rgCurrentIndex >= rgItemsLength){
				rgCurrentIndex = 0;
			}
			setSectionItems(function(i,$item){
				$item.css(rgTansCSS[i]);
			});

			setTimeout(function(){
				isAnimating = false;
			},animatDuration); //防止连击
		}

		opts.$btn_next.on('click',function(e){
			!isAnimating && moveGallery(+1);
			
		});
		opts.$btn_prev.on('click',function(e){
			!isAnimating && moveGallery(-1);
			
		});

		$rgWrapper.on('touchstart',function(e){
			var touch = e.originalEvent.touches[0];
			touchX = touch.pageX;
		}).on('touchend touchcancel',function(e){
			var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0],
				touchGap = touch.pageX - touchX;

			if(touchGap>5){ //swipe right
				opts.$btn_prev.trigger('click');
			}
			if(touchGap<-5){ //swipe left
				opts.$btn_next.trigger('click');
			}

		});
		$(window).on('resize', function(e){
			$rgItems.removeAttr('style'); //清除样式，否则在resize的时候不能正常取到下列元素的width


			rgShowCount = 5;
			rgTansCSS = getTransform3CSS();


			rgCurrentIndex = 0;
			moveGallery(0);
			setTimeout(function(){
				$rgItems.css(getTransitionCSS(animatDuration/1000, 'ease-in-out'));
			},10); //等初始位置设置好后再添加动画

		}).trigger('resize');

		//链式返回
		return this;
    };
    $.fn.responsiveGallery.defaults = {
		animatDuration: 400, //动画时长 单位 ms
		$btn_prev: $('.responsiveGallery-btn_prev'),
		$btn_next: $('.responsiveGallery-btn_next')
    };
})(jQuery);