# Virtual Private Cloud  

A **VPC** is a private, isolated network you create within a cloud provider’s infrastructure — in AWS, it’s your own customizable section of the AWS network.  

### Why VPC?  
1. Your resources are protected from other AWS customers.  
2. Full control over IP ranges, routing, and access.  
3. Can expand with more subnets, gateways  


# Virtual Private Cloud (VPC)

A **Virtual Private Cloud (VPC)** is a private, isolated network created within a cloud provider’s infrastructure.  
In **AWS**, a VPC is your own customizable section of the AWS network.

---

## 🚀 Why VPC?
- Protects your resources from other AWS customers.  
- Full control over **IP ranges, routing, and access**.  
- Scalable with additional **subnets and gateways**.  

---

## 🗂️ Key Components

### **Region & Availability Zones**
- Choose any AWS region with multiple Availability Zones (AZs).
- Define an IP address range for the VPC using **CIDR blocks**.
- Divide into multiple **subnets** (public/private) across AZs.

**Example**:  
- Need ~4000 servers → CIDR block: `10.0.0.0/19`  
- Divide into 6 subnet groups (`/22`) → each with 524 servers.  

---

### **Subnet Types**
- **Public Subnet**: Accessible through the Internet Gateway (IG).  
- **Private Subnet**: Only accessible via servers in the public subnet.  

---

## 🔌 Communication in VPC
- **Internet Gateway (IG):** Entry/exit point to/from the internet.  
- **Router:** Handles communication between subnets.  
- **NAT (Network Address Translation):** Allows private subnet resources to access the internet securely.  
- **NACL (Network Access Control List):** Virtual firewall at the **subnet level** (supports allow + deny rules).  
- **Security Groups (SG):** Firewall at the **instance level** (only allows traffic, default deny).  

**Traffic Flow:**  
