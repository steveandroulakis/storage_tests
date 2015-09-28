#!/usr/bin/python
import matplotlib
matplotlib.use('Agg') #otherwise attemps X11

import glob, os
import numpy as np
import matplotlib.pyplot as plt

def _parse_when(time):
    floatwhen = time.split('/')[-1]
    floatwhen = floatwhen[1:].split('.')[-1]
    fw = floatwhen.split('-')
    floatwhen = '%s-%s-%s %s:%s:%s' % (fw[2], fw[1], fw[0], fw[3], fw[4], fw[5])
    return floatwhen

def get_datapoints(datapoint_dir, threshold=0):
    times = glob.glob(datapoint_dir + "t*")
    times.sort(key=lambda x: os.path.getmtime(x))
    
    floattimes = []
    for time in times:
        filetime = time.split('/')[-1]
        floattime = ('.'.join([str(x) for x in filetime[1:].split('.')[:2]]))
        floatwhen = _parse_when(time)

        if not threshold or float(floattime) < threshold:
            floattimes.append([float(floattime),floatwhen])
        else:
            print "excluded time: %s (threshold: %s)" % (floattime, threshold)
        
    data_points = floattimes
    return data_points

def get_first_time(data_points):
    return data_points[0][1]

#print get_first_time(data_points)

def get_duration(data_points, interval):
    return len(data_points) / (60 / interval) / 60

#print get_duration(data_points, interval)

def get_delays_greater_than(y, seconds):
    # % of bad writes in all
    j = 0
    for i in reversed(y):
        if float(i) > float(seconds):
            j = j + 1

    data_point_count = len(y)
    percentage = (j / float(data_point_count) * 100)
    return {'delayed_writes': j,
            'total_writes': data_point_count,
            'percentage_delayed_writes': percentage}
    
#print get_delays_greater_than(data_points, seconds)

def get_x_from_data_points(data_points):
    return np.arange(len(data_points))
    


def get_y(data_points, length):
    #because different # of data points (dodgy)
    y = np.array(data_points[:length])
    return y[:,0].astype(np.float)



def format_y_for_graph(name, y, color):
    return {'name': name, 'y': y, 'color': color}

def plot_graph(x, y_list, duration, since, delays_greater_than):
    fig = plt.figure(figsize=(15, 12), dpi=80)
    # old matplotlib compat
    #fig.suptitle('Access Times', fontsize=18, fontweight='bold')
    ax = fig.add_subplot(111)

    ax.set_xlabel('time (%i second intervals) over %i hours since %s' %
                  (interval, duration, since), fontsize=14)
    ax.set_ylabel('delay to write file (seconds)', fontsize=14)

    # get a reasonable bounds for y
    max_y_ax = round(y_list[0]['y'].astype(float).max(axis=0))

    # old matplotlib compat # ls='dashed'
    ax.axhline(delay_threshold,color='k')
    ax.set_xlim([0, len(x)])
    ax.set_ylim([0, max_y_ax])
    
    i = 0
    for y_info in y_list:
        ax_align_value = 0.9 + (i * .03)

        ax.text(0.95, ax_align_value, y_info['name'],
                verticalalignment='top', horizontalalignment='right',
                transform=ax.transAxes,
                color=y_info['color'], fontsize=15)

        plt.scatter(x, y_info['y'], c=y_info['color'],
                    alpha=1, s=16, facecolor=y_info['color'], lw = 0)
        
        i = i + 1

    return fig

def generate_figure(dir1, dir2, dir1name, dir2name,
                interval, delay_threshold, outfile):
    
    data_points_dir1 = get_datapoints(dir1, 20) # exclude entries > 20
    y_dir1 = get_y(data_points_dir1, len(data_points_dir1))

    x = get_x_from_data_points(data_points_dir1)

    data_points_dir2 = get_datapoints(dir2)
    y_dir2 = get_y(data_points_dir2, len(data_points_dir1))

    y_list = []

    delay_stats_dir1 = get_delays_greater_than(y_dir1, delay_threshold)
    dir1_delay_text = '(%.2f%%) delayed (>%is) writes' %\
    (delay_stats_dir1['percentage_delayed_writes'], delay_threshold)

    delay_stats_dir2 = get_delays_greater_than(y_dir2, delay_threshold)
    dir2_delay_text = '(%.2f%%) delayed (>%is) writes' %\
    (delay_stats_dir2['percentage_delayed_writes'], delay_threshold)

    y_list.append(format_y_for_graph('%s %s' % (dir1name, dir1_delay_text), y_dir1, 'red'))
    y_list.append(format_y_for_graph('%s %s' % (dir2name, dir2_delay_text), y_dir2, 'blue'))
    
    fig = plot_graph(x, y_list,
            get_duration(data_points_dir2, interval),
            get_first_time(data_points_dir2), delay_threshold)

    fig.savefig(outfile)

interval = 30
delay_threshold = 2
dir1 = "/home/steve/projects/sonas_debug/test2/"
dir1name = 'SONAS'
dir2 = "/notsonas/test2/"
dir2name = 'NeCTAR'
outfile = '/home/steve/www/plot.png'

generate_figure(dir1, dir2, dir1name, dir2name,
               interval, delay_threshold, outfile)
