/****************************************************************
Program to create new process and network namespace.

Need to run binary as root to see namespace creation

Credits : Mahmud Ridwan

Sample output on ubuntu linux:

	root@ip-10-1-136-198:/home/ubuntu/CTCI/namespace_creation_linux# ./a.out
	Original `net` Namespace:
	1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    	link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
	2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP mode DEFAULT group default qlen 1000
    	link/ether 02:6a:5c:07:34:08 brd ff:ff:ff:ff:ff:ff
    	altname enp0s5
	3: ens6: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    	link/ether 02:2b:68:0c:b4:e1 brd ff:ff:ff:ff:ff:ff
    	altname enp0s6
	4: ens7: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    	link/ether 02:22:c8:c8:38:f1 brd ff:ff:ff:ff:ff:ff
    	altname enp0s7


	New `net` Namespace:
	1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    	link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
*****************************************************************/



#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>


static char child_stack[1048576];

static int child_fn() {
  printf("New `net` Namespace:\n");
  system("ip link");
  printf("\n\n");
  return 0;
}

int main() {
  printf("Original `net` Namespace:\n");
  system("ip link");
  printf("\n\n");

  pid_t child_pid = clone(child_fn, child_stack+1048576, CLONE_NEWPID | CLONE_NEWNET | SIGCHLD, NULL);

  waitpid(child_pid, NULL, 0);
  return 0;
}
