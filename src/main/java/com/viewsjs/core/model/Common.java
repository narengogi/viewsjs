package com.viewsjs.core.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Entity
@Data
public abstract class Common implements Serializable {
    @Id
    private String id;
    private Date createdAt;
    private Date updatedAt;
}
