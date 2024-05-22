FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && \
    apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev software-properties-common lsb-release \
    openjdk-17-jdk openjdk-17-jre git

RUN apt-key adv --fetch-keys https://apt.kitware.com/keys/kitware-archive-latest.asc && \
    apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" && \
    apt-get update && \
    apt-get install -y cmake

# Install No Gil Python 3.9
RUN git clone https://github.com/jackyk02/python-nogil && \
    cd python-nogil && \
    ./configure --enable-shared CFLAGS=-fPIC && \
    make -j$(nproc) && \
    make install && \
    ldconfig

RUN python3.9 -m pip install torch ma-gym

# Install LF
RUN git clone https://github.com/lf-lang/lingua-franca.git && \
    cd lingua-franca && \
    git submodule update --init --recursive && \
    ./gradlew assemble

# Clone Github Repo
RUN git clone https://github.com/jackyk02/parallel_rl_benchmarks.git

# Copy policy files and run the program
RUN cd /parallel_rl_benchmarks/6.Multi_Agent_Inference/lf_src_file && \
    /lingua-franca/build/install/lf-cli/bin/lfc trafficv4.lf && \
    cp /parallel_rl_benchmarks/6.Multi_Agent_Inference/marl_4_agents/lf/policy_agent_*.pth /parallel_rl_benchmarks/6.Multi_Agent_Inference/lf_src_file/src-gen/trafficv4

WORKDIR /parallel_rl_benchmarks/6.Multi_Agent_Inference/lf_src_file/src-gen/trafficv4

CMD ["python3.9", "trafficv4.py"]