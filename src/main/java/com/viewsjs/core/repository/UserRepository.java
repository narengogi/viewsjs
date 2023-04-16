package com.viewsjs.core.repository;

import org.springframework.data.repository.CrudRepository;
import com.viewsjs.core.model.User;

public interface UserRepository extends CrudRepository<User, String> {
}
