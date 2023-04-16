package com.viewsjs.core.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

@Entity
@Data
public class User extends Common {
    private String organizationId;
    private String name;
    private String email;

}
