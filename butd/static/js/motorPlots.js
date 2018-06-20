// configuration of charts
    var configPlotVelocityFeedback = {
	    type: 'scatter',
	    data: {
	        datasets: [{
	        	fill: false,
	        	showLine: true,
	        	borderColor: '#ff6384',
	            label: 'velocity 1',
	            data: []
	        },
	        {
	        	fill: false,
	        	showLine: true,
	        	borderColor: '#36a2eb',
	            label: 'velocity 2',
	            data: []
	        },
	        {
	        	fill: false,
	        	showLine: true,
	        	borderColor: '#cc65fe',
	            label: 'velocity 3',
	            data: []
	        },{
	        	fill: false,
	        	showLine: true,
	        	borderColor: '#ffce56',
	            label: 'velocity 4',
	            data: []
	        }]
	    },
	    options: {
	    	animation: {
	    		duration: 0,
	    	},
	    	elements: {
	    		line: {
	    			tension: 0, //no bezier
	    		}
	    	},
	        scales: {
	            yAxes: [{
	                ticks: {
	                    beginAtZero:true
	                }
	            }]
	        }
	    }
	};
    var configPlotOdometryVelocity = {
    	    type: 'scatter',
    	    data: {
    	        datasets: [{
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#ff6384',
    	            label: 'velocity x',
    	            data: []
    	        },
    	        {
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#36a2eb',
    	            label: 'velocity y',
    	            data: []
    	        },
    	        {
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#cc65fe',
    	            label: 'velocity z',
    	            data: []
    	        }]
    	    },
    	    options: {
    	    	animation: {
    	    		duration: 0,
    	    	},
    	    	elements: {
    	    		line: {
    	    			tension: 0, //no bezier
    	    		}
    	    	},
    	        scales: {
    	            yAxes: [{
    	                ticks: {
    	                    beginAtZero:true
    	                }
    	            }]
    	        }
    	    }
    	};
    
    var configPlotOdometryPosition = {
    	    type: 'scatter',
    	    data: {
    	        datasets: [{
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#ff6384',
    	            label: 'position x',
    	            data: []
    	        },
    	        {
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#36a2eb',
    	            label: 'position y',
    	            data: []
    	        },
    	        {
    	        	fill: false,
    	        	showLine: true,
    	        	borderColor: '#cc65fe',
    	            label: 'position z',
    	            data: []
    	        }]
    	    },
    	    options: {
    	    	animation: {
    	    		duration: 0,
    	    	},
    	    	elements: {
    	    		line: {
    	    			tension: 0, //no bezier
    	    		}
    	    	},
    	        scales: {
    	            yAxes: [{
    	                ticks: {
    	                    beginAtZero:true
    	                }
    	            }]
    	        }
    	    }
    	};