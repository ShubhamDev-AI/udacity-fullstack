# Useful Linux Know-How

## Host Configuration

*The central file that controls your resolver setup is `host.conf`. It resides in `/etc/host.conf` and tells the resolver which services to use, and in what order.* - [The host.conf File](https://www.tldp.org/LDP/nag/node82.html)

### DNS Overrides (Hosts)

*Modifying your hosts file enables you to override the DNS for a domain, on that particular machine. This is useful when you want to test your site without the test link, prior to going live with SSL; verify that an alias site works, prior to DNS changes; and for other DNS-related reasons. Modifying your hosts file causes your local machine to look directly at the IP address specified.* - [Modify your hosts file - Rackspace](https://support.rackspace.com/how-to/modify-your-hosts-file/)

**/etc/hosts**

```
127.0.0.1 localhost
# 64.49.219.194 www.domain.com

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
```

## Hostname

*You can use the hostname command to see or set the system’s host name. The host name or computer name is usually at system startup in `/etc/hostname` file.* - [Ubuntu Linux Change Hostname (computer name)](https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/)
